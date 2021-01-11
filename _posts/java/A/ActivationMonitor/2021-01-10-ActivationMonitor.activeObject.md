---
title: ActivationMonitor.activeObject()
permalink: Java/ActivationMonitor/activeObject
date: 2021-01-10
key: JavaJava.A.ActivationMonitor
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationMonitor.metodos valor="activeObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void activeObject(ActivationID id, MarshalledObject<? extends Remote> obj) throws UnknownObjectException, RemoteException
~~~

## Parámetros
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}
* **MarshalledObject&lt;? extends Remote&gt; obj**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject<? extends Remote> obj" %}

## Excepciones
[UnknownObjectException](/Java/UnknownObjectException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[ActivationMonitor](/Java/ActivationMonitor/)

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
