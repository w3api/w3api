---
title: StyleablePropertyFactory.createColorCssMetaData()
permalink: /Java/StyleablePropertyFactory/createColorCssMetaData/
date: 2021-01-11
key: Java.S.StyleablePropertyFactory
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createColorCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CssMetaData<S,Color> createColorCssMetaData(String property, Function<S,StyleableProperty<Color>> function)
public final CssMetaData<S,Color> createColorCssMetaData(String property, Function<S,StyleableProperty<Color>> function, Color initialValue)
public final CssMetaData<S,Color> createColorCssMetaData(String property, Function<S,StyleableProperty<Color>> function, Color initialValue, boolean inherits)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **Color initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Color initialValue" %}
* **StyleableProperty&lt;Color&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<Color>> function" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
