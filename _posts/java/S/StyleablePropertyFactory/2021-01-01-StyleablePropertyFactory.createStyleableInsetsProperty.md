---
title: StyleablePropertyFactory.createStyleableInsetsProperty()
permalink: /Java/StyleablePropertyFactory/createStyleableInsetsProperty/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleableInsetsProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StyleableProperty<Insets> createStyleableInsetsProperty(S styleable, String propertyName, String cssProperty)
public final StyleableProperty<Insets> createStyleableInsetsProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Insets>> function)
public final StyleableProperty<Insets> createStyleableInsetsProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Insets>> function, Insets initialValue)
public final StyleableProperty<Insets> createStyleableInsetsProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Insets>> function, Insets initialValue, boolean inherits)
~~~

## Parámetros
* **Insets initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Insets initialValue" %}
* **String cssProperty**,  {% include w3api/param_description.html metodo=_dato parametro="String cssProperty" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **StyleableProperty&lt;Insets&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Insets>> function" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}
* **S styleable**,  {% include w3api/param_description.html metodo=_dato parametro="S styleable" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StyleablePropertyFactory](/Java/StyleablePropertyFactory/)

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
