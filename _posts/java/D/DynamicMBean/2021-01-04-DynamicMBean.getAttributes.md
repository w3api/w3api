---
title: DynamicMBean.getAttributes()
permalink: Java/DynamicMBean/getAttributes
date: 2021-01-04
key: JavaJava.D.DynamicMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DynamicMBean.metodos valor="getAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AttributeList getAttributes(String[] attributes)
~~~

## Parámetros
* **String[] attributes**,  {% include w3api/param_description.html metodo=_data parametro="String[] attributes" %}

## Clase Padre
[DynamicMBean](/Java/DynamicMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DynamicMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
