---
title: StringProperty.bindBidirectional()
permalink: Java/StringProperty/bindBidirectional
date: 2021-01-04
key: JavaJava.S.StringProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StringProperty.metodos valor="bindBidirectional" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void bindBidirectional(Property<?> other, Format format)
<T> void bindBidirectional(Property<T> other, StringConverter<T> converter)
~~~

## Parámetros
* **StringConverter&lt;T&gt; converter**,  {% include w3api/param_description.html metodo=_data parametro="StringConverter<T> converter" %}
* **Property&lt;T&gt; other**,  {% include w3api/param_description.html metodo=_data parametro="Property<T> other" %}
* **Property&lt;?&gt; other**,  {% include w3api/param_description.html metodo=_data parametro="Property<?> other" %}
* **Format format**,  {% include w3api/param_description.html metodo=_data parametro="Format format" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StringProperty](/Java/StringProperty/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
