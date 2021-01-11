---
title: UnicastRemoteObject.UnicastRemoteObject()
permalink: Java/UnicastRemoteObject/UnicastRemoteObject
date: 2021-01-11
key: JavaJava.U.UnicastRemoteObject
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UnicastRemoteObject.constructores valor="UnicastRemoteObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected UnicastRemoteObject() throws RemoteException
protected UnicastRemoteObject(int port) throws RemoteException
protected UnicastRemoteObject(int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws RemoteException
~~~

## Parámetros
* **RMIClientSocketFactory csf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIClientSocketFactory csf" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **RMIServerSocketFactory ssf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIServerSocketFactory ssf" %}

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
