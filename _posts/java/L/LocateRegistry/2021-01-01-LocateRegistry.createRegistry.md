---
title: LocateRegistry.createRegistry()
permalink: /Java/LocateRegistry/createRegistry/
date: 2021-01-11
key: Java.L.LocateRegistry
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
* **RMIClientSocketFactory csf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIClientSocketFactory csf" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **RMIServerSocketFactory ssf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIServerSocketFactory ssf" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
