---
title: LocateRegistry.createRegistry()
permalink: Java/LocateRegistry/createRegistry
date: 2021-01-04
key: JavaJava.L.LocateRegistry
category: java
tags: ['java se', 'java.rmi.registry', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocateRegistry.metodos valor="createRegistry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Registry createRegistry(int port) throws RemoteException
public static Registry createRegistry(int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws RemoteException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **RMIClientSocketFactory csf**,  {% include w3api/param_description.html metodo=_data parametro="RMIClientSocketFactory csf" %}
* **RMIServerSocketFactory ssf**,  {% include w3api/param_description.html metodo=_data parametro="RMIServerSocketFactory ssf" %}

## Excepciones
[RemoteException](/Java/RemoteException/)

## Clase Padre
[LocateRegistry](/Java/LocateRegistry/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocateRegistry.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
