---
title: InternalFrameFocusTraversalPolicy.getInitialComponent()
permalink: /Java/InternalFrameFocusTraversalPolicy/getInitialComponent/
date: 2021-01-11
key: Java.I.InternalFrameFocusTraversalPolicy
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InternalFrameFocusTraversalPolicy.metodos valor="getInitialComponent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Component getInitialComponent(JInternalFrame frame)
~~~

## Parámetros
* **JInternalFrame frame**,  {% include w3api/param_description.html metodo=_dato parametro="JInternalFrame frame" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InternalFrameFocusTraversalPolicy](/Java/InternalFrameFocusTraversalPolicy/)

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
