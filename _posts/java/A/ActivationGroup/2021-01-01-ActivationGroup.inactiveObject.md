---
title: ActivationGroup.inactiveObject()
permalink: /Java/ActivationGroup/inactiveObject/
date: 2021-01-11
key: Java.A.ActivationGroup
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationGroup.metodos valor="inactiveObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean inactiveObject(ActivationID id) throws ActivationException, UnknownObjectException, RemoteException
~~~

## Parámetros
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [UnknownObjectException](/Java/UnknownObjectException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[ActivationGroup](/Java/ActivationGroup/)

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
