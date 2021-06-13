---
title: RequiredModelMBean.RequiredModelMBean()
permalink: /Java/RequiredModelMBean/RequiredModelMBean/
date: 2021-01-11
key: Java.R.RequiredModelMBean
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RequiredModelMBean.constructores valor="RequiredModelMBean" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RequiredModelMBean() throws MBeanException, RuntimeOperationsException
public RequiredModelMBean(ModelMBeanInfo mbi) throws MBeanException, RuntimeOperationsException
~~~

## Parámetros
* **ModelMBeanInfo mbi**,  {% include w3api/param_description.html metodo=_dato parametro="ModelMBeanInfo mbi" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[RequiredModelMBean](/Java/RequiredModelMBean/)

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
