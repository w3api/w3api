---
title: GSSManager.getMechsForName()
permalink: Java/GSSManager/getMechsForName
date: 2021-01-04
key: JavaJava.G.GSSManager
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSManager.metodos valor="getMechsForName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Oid[] getMechsForName(Oid nameType)
~~~

## Parámetros
* **Oid nameType**,  {% include w3api/param_description.html metodo=_data parametro="Oid nameType" %}

## Clase Padre
[GSSManager](/Java/GSSManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GSSManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
