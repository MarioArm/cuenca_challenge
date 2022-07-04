# Cuenca Challenge - N-queen puzzle solver

## Description

This project is a puzzle solver for the N-queen puzzle. Specifically, it is processing the solutions for a different number
of queens starting with 8 queens, and it automatically stops when at the end of a solution if the time has already
surpassed 10 minutes. The results of every solution will be stored on a DB.

This project is using the solution from
[Techie Delight - print-possible-solutions-n-queens-problem](https://www.techiedelight.com/print-possible-solutions-n-queens-problem/)
but instead of printing the chessboard to the stdout **it is counting the possible solutions and persisting the
solutions to a DB on PostgreSQL**.

## Running the project

This project is using **docker-compose** to easily download and deploy all the dependencies, run tests and execute the
program. So you only have to run the following:
> docker-compose up

This will do all for you, and you can take a cup of coffee in the time it takes to finish.
> Note: Even though it is programmed to end **after** 10 minutes, it will continue running until the current
> board size is finished. So it is recommended to finish it manually since you can check the results on the DB afterward.

### Check results on DB

To review the results from the DB you can connect with your favorite SQL client using the following info:

```YAML
PostgreSQL
host: localhost
port: 5432
database: solutions
user: root
password: root
```

## Travis CI

Every PR is required to pass the validations from Travis
CI [as you can see here](https://github.com/MarioArm/cuenca_challenge/runs/7186470941). Right now the only validation is
to pass all the tests created with pytest
