---
title: TableColumnBase.getCellObservableValue()
permalink: Java/TableColumnBase/getCellObservableValue
date: 2021-01-04
key: JavaJava.T.TableColumnBase
category: java
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
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **S item**,  {% include w3api/param_description.html metodo=_data parametro="S item" %}

## Clase Padre
[TableColumnBase](/Java/TableColumnBase/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableColumnBase.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
