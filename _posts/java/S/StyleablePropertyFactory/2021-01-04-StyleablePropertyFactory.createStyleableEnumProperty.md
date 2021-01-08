---
title: StyleablePropertyFactory.createStyleableEnumProperty()
permalink: Java/StyleablePropertyFactory/createStyleableEnumProperty
date: 2021-01-04
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleableEnumProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<E extends Enum<E>>StyleableProperty<E> createStyleableEnumProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<E>> function, Class<E> enumClass)
<E extends Enum<E>>StyleableProperty<E> createStyleableEnumProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<E>> function, Class<E> enumClass, E initialValue)
<E extends Enum<E>>StyleableProperty<E> createStyleableEnumProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<E>> function, Class<E> enumClass, E initialValue, boolean inherits)
~~~

## Parámetros
* **String cssProperty**,  {% include w3api/param_description.html metodo=_data parametro="String cssProperty" %}
* **StyleableProperty&lt;E&gt;&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="StyleableProperty<E>> function" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **Class&lt;E&gt; enumClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<E> enumClass" %}
* **E initialValue**,  {% include w3api/param_description.html metodo=_data parametro="E initialValue" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **S styleable**,  {% include w3api/param_description.html metodo=_data parametro="S styleable" %}

## Clase Padre
[StyleablePropertyFactory](/Java/StyleablePropertyFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StyleablePropertyFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
