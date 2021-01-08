---
title: DefaultTableModel.setDataVector()
permalink: Java/DefaultTableModel/setDataVector
date: 2021-01-04
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
* **Object[][] dataVector**,  {% include w3api/param_description.html metodo=_data parametro="Object[][] dataVector" %}
* **Object[] columnIdentifiers**,  {% include w3api/param_description.html metodo=_data parametro="Object[] columnIdentifiers" %}
* **Vector&lt;? extends Vector&gt; dataVector**,  {% include w3api/param_description.html metodo=_data parametro="Vector<? extends Vector> dataVector" %}
* **Vector&lt;?&gt; columnIdentifiers**,  {% include w3api/param_description.html metodo=_data parametro="Vector<?> columnIdentifiers" %}

## Clase Padre
[DefaultTableModel](/Java/DefaultTableModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultTableModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
