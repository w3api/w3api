---
title: DefaultTreeModel.getListeners()
permalink: /Java/DefaultTreeModel/getListeners/
date: 2021-01-11
key: Java.D.DefaultTreeModel
category: Java
tags: ['java se', 'javax.swing.tree', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTreeModel.metodos valor="getListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends EventListener>T[] getListeners(Class<T> listenerType)
~~~

## Parámetros
* **Class&lt;T&gt; listenerType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> listenerType" %}

## Clase Padre
[DefaultTreeModel](/Java/DefaultTreeModel/)

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
