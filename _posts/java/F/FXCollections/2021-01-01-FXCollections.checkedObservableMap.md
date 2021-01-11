---
title: FXCollections.checkedObservableMap()
permalink: Java/FXCollections/checkedObservableMap
date: 2021-01-11
key: JavaJava.F.FXCollections
category: java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FXCollections.metodos valor="checkedObservableMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <K,V> ObservableMap<K,V> checkedObservableMap(ObservableMap<K,V> map, Class<K> keyType, Class<V> valueType)
~~~

## Parámetros
* **ObservableMap&lt;K**,  {% include w3api/param_description.html metodo=_dato parametro="ObservableMap<K" %}
* **Class&lt;V&gt; valueType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<V> valueType" %}
* **Class&lt;K&gt; keyType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<K> keyType" %}
* **V&gt; map**,  {% include w3api/param_description.html metodo=_dato parametro="V> map" %}

## Clase Padre
[FXCollections](/Java/FXCollections/)

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
