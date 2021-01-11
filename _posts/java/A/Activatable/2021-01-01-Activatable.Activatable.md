---
title: Activatable.Activatable()
permalink: Java/Activatable/Activatable
date: 2021-01-11
key: JavaJava.A.Activatable
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Activatable.constructores valor="Activatable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Activatable(String location, MarshalledObject<?> data, boolean restart, int port) throws ActivationException, RemoteException
protected Activatable(String location, MarshalledObject<?> data, boolean restart, int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws ActivationException, RemoteException
protected Activatable(ActivationID id, int port) throws RemoteException
protected Activatable(ActivationID id, int port, RMIClientSocketFactory csf, RMIServerSocketFactory ssf) throws RemoteException
~~~

## Parámetros
* **RMIClientSocketFactory csf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIClientSocketFactory csf" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **boolean restart**,  {% include w3api/param_description.html metodo=_dato parametro="boolean restart" %}
* **String location**,  {% include w3api/param_description.html metodo=_dato parametro="String location" %}
* **RMIServerSocketFactory ssf**,  {% include w3api/param_description.html metodo=_dato parametro="RMIServerSocketFactory ssf" %}
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}
* **MarshalledObject&lt;?&gt; data**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject<?> data" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [RemoteException](/Java/RemoteException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[Activatable](/Java/Activatable/)

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
