---
title: ActivationMonitor.activeObject()
permalink: Java/ActivationMonitor/activeObject
date: 2021-01-04
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
* **ActivationID id**,  {% include w3api/param_description.html metodo=_data parametro="ActivationID id" %}
* **MarshalledObject&lt;? extends Remote&gt; obj**,  {% include w3api/param_description.html metodo=_data parametro="MarshalledObject<? extends Remote> obj" %}

## Excepciones
[RemoteException](/Java/RemoteException/), [UnknownObjectException](/Java/UnknownObjectException/)

## Clase Padre
[ActivationMonitor](/Java/ActivationMonitor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ActivationMonitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
