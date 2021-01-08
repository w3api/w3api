---
title: SimpleDoc.SimpleDoc()
permalink: Java/SimpleDoc/SimpleDoc
date: 2021-01-04
key: JavaJava.S.SimpleDoc
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleDoc.constructores valor="SimpleDoc" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SimpleDoc(Object printData, DocFlavor flavor, DocAttributeSet attributes)
~~~

## Parámetros
* **DocAttributeSet attributes**,  {% include w3api/param_description.html metodo=_data parametro="DocAttributeSet attributes" %}
* **DocFlavor flavor**,  {% include w3api/param_description.html metodo=_data parametro="DocFlavor flavor" %}
* **Object printData**,  {% include w3api/param_description.html metodo=_data parametro="Object printData" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SimpleDoc](/Java/SimpleDoc/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleDoc.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
