---
title: TableColumnBase.getCellObservableValue()
permalink: /Java/TableColumnBase/getCellObservableValue/
date: 2021-01-11
key: Java.T.TableColumnBase
category: Java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableColumnBase.metodos valor="getCellObservableValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract ObservableValue<T> getCellObservableValue(int index)
public abstract ObservableValue<T> getCellObservableValue(S item)
~~~

## Parámetros
* **S item**,  {% include w3api/param_description.html metodo=_dato parametro="S item" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Clase Padre
[TableColumnBase](/Java/TableColumnBase/)

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
