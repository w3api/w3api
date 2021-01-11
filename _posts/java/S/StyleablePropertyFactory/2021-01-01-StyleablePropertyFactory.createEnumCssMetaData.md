---
title: StyleablePropertyFactory.createEnumCssMetaData()
permalink: Java/StyleablePropertyFactory/createEnumCssMetaData
date: 2021-01-11
key: JavaJava.S.StyleablePropertyFactory
category: java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleablePropertyFactory.metodos valor="createEnumCssMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<E extends Enum<E>>CssMetaData<S,E> createEnumCssMetaData(Class<? extends Enum> enumClass, String property, Function<S,StyleableProperty<E>> function)
<E extends Enum<E>>CssMetaData<S,E> createEnumCssMetaData(Class<? extends Enum> enumClass, String property, Function<S,StyleableProperty<E>> function, E initialValue)
<E extends Enum<E>>CssMetaData<S,E> createEnumCssMetaData(Class<? extends Enum> enumClass, String property, Function<S,StyleableProperty<E>> function, E initialValue, boolean inherits)
~~~

## Parámetros
* **String property**,  {% include w3api/param_description.html metodo=_dato parametro="String property" %}
* **StyleableProperty&lt;E&gt;&gt; function**,  {% include w3api/param_description.html metodo=_dato parametro="StyleableProperty<E>> function" %}
* **Class&lt;? extends Enum&gt; enumClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends Enum> enumClass" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_dato parametro="boolean inherits" %}
* **E initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="E initialValue" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}

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
