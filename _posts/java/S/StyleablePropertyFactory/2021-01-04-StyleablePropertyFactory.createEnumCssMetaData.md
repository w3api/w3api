---
title: StyleablePropertyFactory.createEnumCssMetaData()
permalink: Java/StyleablePropertyFactory/createEnumCssMetaData
date: 2021-01-04
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
* **StyleableProperty&lt;E&gt;&gt; function**,  {% include w3api/param_description.html metodo=_data parametro="StyleableProperty<E>> function" %}
* **boolean inherits**,  {% include w3api/param_description.html metodo=_data parametro="boolean inherits" %}
* **E initialValue**,  {% include w3api/param_description.html metodo=_data parametro="E initialValue" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **Class&lt;? extends Enum&gt; enumClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<? extends Enum> enumClass" %}
* **String property**,  {% include w3api/param_description.html metodo=_data parametro="String property" %}

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
