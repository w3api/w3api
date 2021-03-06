---
title: ActivationGroup.createGroup()
permalink: /Java/ActivationGroup/createGroup/
date: 2021-01-11
key: Java.A.ActivationGroup
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationGroup.metodos valor="createGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ActivationGroup createGroup(ActivationGroupID id, ActivationGroupDesc desc, long incarnation) throws ActivationException
~~~

## Parámetros
* **long incarnation**,  {% include w3api/param_description.html metodo=_dato parametro="long incarnation" %}
* **ActivationGroupDesc desc**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupDesc desc" %}
* **ActivationGroupID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupID id" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
