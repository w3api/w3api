---
title: GSSManager.getNamesForMech()
permalink: /Java/GSSManager/getNamesForMech/
date: 2021-01-11
key: Java.G.GSSManager
category: Java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSManager.metodos valor="getNamesForMech" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Oid[] getNamesForMech(Oid mech) throws GSSException
~~~

## Parámetros
* **Oid mech**,  {% include w3api/param_description.html metodo=_dato parametro="Oid mech" %}

## Excepciones
[GSSException](/Java/GSSException/)

## Clase Padre
[GSSManager](/Java/GSSManager/)

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
