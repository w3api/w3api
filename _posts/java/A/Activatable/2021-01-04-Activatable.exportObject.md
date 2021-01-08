---
title: Activatable.exportObject()
permalink: Java/Activatable/exportObject
date: 2021-01-04
key: JavaJava.A.Activatable
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Activatable.metodos valor="exportObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ActivationID exportObject(Remote obj, String location, MarshalledObject<?> data, boolean restart, int port) throws ActivationException, RemoteException
public static ActivationID exportObject(Remote obj, String location, MarshalledObject<?> data, boolean restart, int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws ActivationException, RemoteException
public static Remote exportObject(Remote obj, ActivationID id, int port) throws RemoteException
public static Remote exportObject(Remote obj, ActivationID id, int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws RemoteException
~~~

## Parámetros
* **RMIClientSocketFactory csf**,  {% include w3api/param_description.html metodo=_data parametro="RMIClientSocketFactory csf" %}
* **boolean restart**,  {% include w3api/param_description.html metodo=_data parametro="boolean restart" %}
* **String location**,  {% include w3api/param_description.html metodo=_data parametro="String location" %}
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **Remote obj**,  {% include w3api/param_description.html metodo=_data parametro="Remote obj" %}
* **RMIServerSocketFactory ssf**,  {% include w3api/param_description.html metodo=_data parametro="RMIServerSocketFactory ssf" %}
* **MarshalledObject&lt;?&gt; data**,  {% include w3api/param_description.html metodo=_data parametro="MarshalledObject<?> data" %}
* **ActivationID id**,  {% include w3api/param_description.html metodo=_data parametro="ActivationID id" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[Activatable](/Java/Activatable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.Activatable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
