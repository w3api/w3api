---
title: FocusTraversalPolicy.getDefaultComponent()
permalink: /Java/FocusTraversalPolicy/getDefaultComponent/
date: 2021-01-11
key: Java.F.FocusTraversalPolicy
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FocusTraversalPolicy.metodos valor="getDefaultComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Component getDefaultComponent(Container aContainer)
~~~

## Parámetros
* **Container aContainer**,  {% include w3api/param_description.html metodo=_dato parametro="Container aContainer" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FocusTraversalPolicy](/Java/FocusTraversalPolicy/)

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
