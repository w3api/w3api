---
title: FocusTraversalPolicy.getComponentBefore()
permalink: Java/FocusTraversalPolicy/getComponentBefore
date: 2021-01-11
key: JavaJava.F.FocusTraversalPolicy
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FocusTraversalPolicy.metodos valor="getComponentBefore" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Component getComponentBefore(Container aContainer, Component aComponent)
~~~

## Parámetros
* **Container aContainer**,  {% include w3api/param_description.html metodo=_dato parametro="Container aContainer" %}
* **Component aComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component aComponent" %}

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
