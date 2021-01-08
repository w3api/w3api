---
title: KeyboardFocusManager.setGlobalPermanentFocusOwner()
permalink: Java/KeyboardFocusManager/setGlobalPermanentFocusOwner
date: 2021-01-04
key: JavaJava.K.KeyboardFocusManager
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyboardFocusManager.metodos valor="setGlobalPermanentFocusOwner" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void setGlobalPermanentFocusOwner(Component permanentFocusOwner) throws SecurityException
~~~

## Parámetros
* **Component permanentFocusOwner**,  {% include w3api/param_description.html metodo=_data parametro="Component permanentFocusOwner" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[KeyboardFocusManager](/Java/KeyboardFocusManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyboardFocusManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
