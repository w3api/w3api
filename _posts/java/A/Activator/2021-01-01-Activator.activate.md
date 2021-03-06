---
title: Activator.activate()
permalink: /Java/Activator/activate/
date: 2021-01-11
key: Java.A.Activator
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Activator.metodos valor="activate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
MarshalledObject<? extends Remote> activate(ActivationID id, boolean force) throws ActivationException, UnknownObjectException, RemoteException
~~~

## Parámetros
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}
* **boolean force**,  {% include w3api/param_description.html metodo=_dato parametro="boolean force" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [UnknownObjectException](/Java/UnknownObjectException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[Activator](/Java/Activator/)

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
