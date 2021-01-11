---
title: ObjectExpression.asString()
permalink: Java/ObjectExpression/asString
date: 2021-01-11
key: JavaJava.O.ObjectExpression
category: java
tags: ['java se', 'javafx.beans.binding', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectExpression.metodos valor="asString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringBinding asString()
public StringBinding asString(String format)
public StringBinding asString(Locale locale, String format)
~~~

## Parámetros
* **String format**,  {% include w3api/param_description.html metodo=_dato parametro="String format" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Clase Padre
[ObjectExpression](/Java/ObjectExpression/)

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
