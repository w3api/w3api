---
title: ActivationSystem.registerGroup()
permalink: Java/ActivationSystem/registerGroup
date: 2021-01-10
key: JavaJava.A.ActivationSystem
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationSystem.metodos valor="registerGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ActivationGroupID registerGroup(ActivationGroupDesc desc) throws ActivationException, RemoteException
~~~

## Parámetros
* **ActivationGroupDesc desc**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupDesc desc" %}

## Excepciones
[RemoteException](/Java/RemoteException/), [ActivationException](/Java/ActivationException/)

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
