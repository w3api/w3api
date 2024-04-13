---
title: ModelMBeanInfo.getAttribute()
permalink: /Java/ModelMBeanInfo/getAttribute/
date: 2021-01-11
key: Java.M.ModelMBeanInfo
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanInfo.metodos valor="getAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ModelMBeanAttributeInfo getAttribute(String inName) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **String inName**,  {% include w3api/param_description.html metodo=_dato parametro="String inName" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanInfo](/Java/ModelMBeanInfo/)

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
