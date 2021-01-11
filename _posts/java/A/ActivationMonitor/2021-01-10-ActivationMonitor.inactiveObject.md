---
title: ActivationMonitor.inactiveObject()
permalink: Java/ActivationMonitor/inactiveObject
date: 2021-01-10
key: JavaJava.A.ActivationMonitor
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationMonitor.metodos valor="inactiveObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void inactiveObject(ActivationID id) throws UnknownObjectException, RemoteException
~~~

## Parámetros
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}

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
