---
title: ContainerOrderFocusTraversalPolicy.getComponentAfter()
permalink: /Java/ContainerOrderFocusTraversalPolicy/getComponentAfter/
date: 2021-01-11
key: Java.C.ContainerOrderFocusTraversalPolicy
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContainerOrderFocusTraversalPolicy.metodos valor="getComponentAfter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component getComponentAfter(Container aContainer, Component aComponent)
~~~

## Parámetros
* **Container aContainer**,  {% include w3api/param_description.html metodo=_dato parametro="Container aContainer" %}
* **Component aComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component aComponent" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ContainerOrderFocusTraversalPolicy](/Java/ContainerOrderFocusTraversalPolicy/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
