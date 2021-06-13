---
title: LocateRegistry.getRegistry()
permalink: /Java/LocateRegistry/getRegistry/
date: 2021-01-11
key: Java.L.LocateRegistry
category: java
tags: ['java se', 'java.rmi.registry', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocateRegistry.metodos valor="getRegistry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Registry getRegistry() throws RemoteException
public static Registry getRegistry(int port) throws RemoteException
public static Registry getRegistry(String host) throws RemoteException
public static Registry getRegistry(String host, int port) throws RemoteException
public static Registry getRegistry(String host, int port, RMIClientSocketFactory csf) throws RemoteException
~~~

## Parámetros
* **RMIClientSocketFactory csf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIClientSocketFactory csf" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}

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
