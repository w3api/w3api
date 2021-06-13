---
title: ObservableListBase.nextRemove()
permalink: /Java/ObservableListBase/nextRemove/
date: 2021-01-11
key: Java.O.ObservableListBase
category: Java
tags: ['java se', 'javafx.collections', 'javafx.base', 'metodo java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObservableListBase.metodos valor="nextRemove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void nextRemove(int idx, E removed)
protected void nextRemove(int idx, List<? extends E> removed)
~~~

## Parámetros
* **E removed**,  {% include w3api/param_description.html metodo=_dato parametro="E removed" %}
* **int idx**,  {% include w3api/param_description.html metodo=_dato parametro="int idx" %}
* **List&lt;? extends E&gt; removed**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends E> removed" %}

## Clase Padre
[ObservableListBase](/Java/ObservableListBase/)

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
