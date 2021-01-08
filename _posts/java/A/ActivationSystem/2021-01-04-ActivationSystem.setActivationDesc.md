---
title: ActivationSystem.setActivationDesc()
permalink: Java/ActivationSystem/setActivationDesc
date: 2021-01-04
key: JavaJava.A.ActivationSystem
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationSystem.metodos valor="setActivationDesc" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ActivationDesc setActivationDesc(ActivationID id, ActivationDesc desc) throws ActivationException, UnknownObjectException, UnknownGroupException, RemoteException
~~~

## Parámetros
* **ActivationID id**,  {% include w3api/param_description.html metodo=_data parametro="ActivationID id" %}
* **ActivationDesc desc**,  {% include w3api/param_description.html metodo=_data parametro="ActivationDesc desc" %}

## Excepciones
[RemoteException](/Java/RemoteException/), [ActivationException](/Java/ActivationException/), [UnknownGroupException](/Java/UnknownGroupException/), [UnknownObjectException](/Java/UnknownObjectException/)

## Clase Padre
[ActivationSystem](/Java/ActivationSystem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ActivationSystem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
