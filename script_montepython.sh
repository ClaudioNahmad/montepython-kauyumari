### Carga las variables de ambiente
#PBS -V

### Nombre del trabajo
#PBS -N class-cpl

### Que tipo de cola vamos a usar para enviar el trabajo 
### (hasta ahora se que existen pq1a y desiq1i)
#PBS -q desiq1i

### Usa el shell bourne
#PBS -S /bin/sh

### Salidas de error y de log, con nombre
#PBS -e cpl_err.err
#PBS -o cpl_log.log

### Numero de nodos y de cores por nodo (ppn)
#PBS -l nodes=2:ppn=16

###  esto no se que significa, preguntarle a erick o investigar
#PBS -W x=nmatchpolicy=exactnode


cd $PBS_O_WORKDIR
echo Working directory is $PBS_O_WORKDIR

### Calcula numero de procesadores y nodos reservados para esta corrida
NPROCS=`wc -l < $PBS_NODEFILE`
NNODES=`uniq $PBS_NODEFILE | wc -l`

### Despliega el contexto del trabajo
echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo Using ${NPROCS} processors across ${NNODES} nodes

###Esta seccion es para programas hibridos que corran MPI con openMP
### (algo que hace erick con camb), comentar si no se va a usar
### OMP_NUM_THREADS=$PBS_NUM_PPN
### export OMP_NUM_THREADS
### export OMPI_MCA_btl="openib,self,sm"


###mpirun -npernode 1 ./cosmomc test.ini
###mpirun --map-by ppr:1:socket ./cosmomc test.ini
mpirun -np 16 python montepython/MontePython.py run -p cpl.param --conf class-cpl.conf -o chains/atocatl_parallel1 -N 20000

