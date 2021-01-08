---
title: StyleablePropertyFactory.createStyleableColorProperty()
permalink: Java/StyleablePropertyFactory/createStyleableColorProperty
date: 2021-01-04
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createStyleableColorProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StyleableProperty<Color> createStyleableColorProperty(S styleable, String propertyName, String cssProperty)
public final StyleableProperty<Color> createStyleableColorProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Color>> function)
public final StyleableProperty<Color> createStyleableColorProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Color>> function, Color initialValue)
public final StyleableProperty<Color> createStyleableColorProperty(S styleable, String propertyName, String cssProperty, Function<S,StyleableProperty<Color>> function, Color initialValue, boolean inherits)
~~~

## Parámetros
* **String cssProperty**,  {% include w3api/param_description.html metodo=_data parametro="String cssProperty" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}
* **StyleableProperty&lt;Color&gt;&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="StyleableProperty<Color>> function" %}
* **Color initialValue**,  {% include w3api/param_description.html metodo=_data parametro="Color initialValue" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **S styleable**,  {% include w3api/param_description.html metodo=_data parametro="S styleable" %}

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
{%- for _ldc in site.data.Java.S.StyleablePropertyFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
