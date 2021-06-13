---
title: ModelMBean.setModelMBeanInfo()
permalink: /Java/ModelMBean/setModelMBeanInfo/
date: 2021-01-11
key: Java.M.ModelMBean
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBean.metodos valor="setModelMBeanInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setModelMBeanInfo(ModelMBeanInfo inModelMBeanInfo) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **ModelMBeanInfo inModelMBeanInfo**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanInfo inModelMBeanInfo" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[ModelMBean](/Java/ModelMBean/)

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
