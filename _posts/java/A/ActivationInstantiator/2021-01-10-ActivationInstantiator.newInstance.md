---
title: ActivationInstantiator.newInstance()
permalink: Java/ActivationInstantiator/newInstance
date: 2021-01-10
key: JavaJava.A.ActivationInstantiator
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationInstantiator.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
MarshalledObject<? extends Remote> newInstance(ActivationID id, ActivationDesc desc) throws ActivationException, RemoteException
~~~

## Parámetros
* **ActivationDesc desc**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationDesc desc" %}
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}

## Excepciones
[RemoteException](/Java/RemoteException/), [ActivationException](/Java/ActivationException/)

## Clase Padre
[ActivationInstantiator](/Java/ActivationInstantiator/)

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
