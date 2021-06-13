---
title: ModelMBeanInfoSupport.getConstructor()
permalink: Java/ModelMBeanInfoSupport/getConstructor
date: 2021-01-11
key: JavaJava.M.ModelMBeanInfoSupport
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBeanInfoSupport.metodos valor="getConstructor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ModelMBeanConstructorInfo getConstructor(String inName) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **String inName**,  {% include w3api/param_description.html metodo=_dato parametro="String inName" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBeanInfoSupport](/Java/ModelMBeanInfoSupport/)

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
