---
title: ActivationSystem.setActivationGroupDesc()
permalink: Java/ActivationSystem/setActivationGroupDesc
date: 2021-01-10
key: JavaJava.A.ActivationSystem
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationSystem.metodos valor="setActivationGroupDesc" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ActivationGroupDesc setActivationGroupDesc(ActivationGroupID id, ActivationGroupDesc desc) throws ActivationException, UnknownGroupException, RemoteException
~~~

## Parámetros
* **ActivationGroupDesc desc**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupDesc desc" %}
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
