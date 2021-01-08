---
title: ActivationInstantiator.newInstance()
permalink: Java/ActivationInstantiator/newInstance
date: 2021-01-04
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
* **ActivationID id**,  {% include w3api/param_description.html metodo=_data parametro="ActivationID id" %}
* **ActivationDesc desc**,  {% include w3api/param_description.html metodo=_data parametro="ActivationDesc desc" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[ActivationInstantiator](/Java/ActivationInstantiator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ActivationInstantiator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
