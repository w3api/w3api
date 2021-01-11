---
title: ActivationSystem.registerObject()
permalink: Java/ActivationSystem/registerObject
date: 2021-01-11
key: JavaJava.A.ActivationSystem
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationSystem.metodos valor="registerObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ActivationID registerObject(ActivationDesc desc) throws ActivationException, UnknownGroupException, RemoteException
~~~

## Parámetros
* **ActivationDesc desc**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationDesc desc" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [UnknownGroupException](/Java/UnknownGroupException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[ActivationSystem](/Java/ActivationSystem/)

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
