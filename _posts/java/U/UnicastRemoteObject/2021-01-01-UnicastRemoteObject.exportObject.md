---
title: UnicastRemoteObject.exportObject()
permalink: Java/UnicastRemoteObject/exportObject
date: 2021-01-11
key: JavaJava.U.UnicastRemoteObject
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UnicastRemoteObject.metodos valor="exportObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public static RemoteStub exportObject(Remote obj) throws RemoteException
public static Remote exportObject(Remote obj, int port) throws RemoteException
public static Remote exportObject(Remote obj, int port, ObjectInputFilter filter) throws RemoteException
public static Remote exportObject(Remote obj, int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws RemoteException
public static Remote exportObject(Remote obj, int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf, ObjectInputFilter filter) throws RemoteException
~~~

## Parámetros
* **Remote obj**,  {% include w3api/param_description.html metodo=_dato parametro="Remote obj" %}
* **RMIClientSocketFactory csf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIClientSocketFactory csf" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **RMIServerSocketFactory ssf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIServerSocketFactory ssf" %}
* **ObjectInputFilter filter**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectInputFilter filter" %}

## Excepciones
[RemoteException](/Java/RemoteException/)

## Clase Padre
[UnicastRemoteObject](/Java/UnicastRemoteObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
