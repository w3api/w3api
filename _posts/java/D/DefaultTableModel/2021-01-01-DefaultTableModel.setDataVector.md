---
title: DefaultTableModel.setDataVector()
permalink: Java/DefaultTableModel/setDataVector
date: 2021-01-11
key: JavaJava.D.DefaultTableModel
category: java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultTableModel.metodos valor="setDataVector" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setDataVector(Object[][] dataVector, Object[] columnIdentifiers)
public void setDataVector(Vector<? extends Vector> dataVector, Vector<?> columnIdentifiers)
~~~

## Parámetros
* **Object[] columnIdentifiers**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] columnIdentifiers" %}
* **Object[][] dataVector**,  {% include w3api/param_description.html metodo=_dato parametro="Object[][] dataVector" %}
* **Vector&lt;? extends Vector&gt; dataVector**,  {% include w3api/param_description.html metodo=_dato parametro="Vector<? extends Vector> dataVector" %}
* **Vector&lt;?&gt; columnIdentifiers**,  {% include w3api/param_description.html metodo=_dato parametro="Vector<?> columnIdentifiers" %}

## Clase Padre
[DefaultTableModel](/Java/DefaultTableModel/)

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