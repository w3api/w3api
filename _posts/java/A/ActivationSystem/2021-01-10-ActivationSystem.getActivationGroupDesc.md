---
title: ActivationSystem.getActivationGroupDesc()
permalink: Java/ActivationSystem/getActivationGroupDesc
date: 2021-01-10
key: JavaJava.A.ActivationSystem
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationSystem.metodos valor="getActivationGroupDesc" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ActivationGroupDesc getActivationGroupDesc(ActivationGroupID id) throws ActivationException, UnknownGroupException, RemoteException
~~~

## Parámetros
* **ActivationGroupID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupID id" %}

## Excepciones
[RemoteException](/Java/RemoteException/), [UnknownGroupException](/Java/UnknownGroupException/), [ActivationException](/Java/ActivationException/)

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
