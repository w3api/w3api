---
title: FXCollections.checkedObservableMap()
permalink: Java/FXCollections/checkedObservableMap
date: 2021-01-04
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
* **ObservableMap&lt;K**,  {% include w3api/param_description.html metodo=_data parametro="ObservableMap<K" %}
* **Class&lt;K&gt; keyType**,  {% include w3api/param_description.html metodo=_data parametro="Class<K> keyType" %}
* **Class&lt;V&gt; valueType**,  {% include w3api/param_description.html metodo=_data parametro="Class<V> valueType" %}
* **V&gt; map**,  {% include w3api/param_description.html metodo=_data parametro="V> map" %}

## Clase Padre
[FXCollections](/Java/FXCollections/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FXCollections.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
