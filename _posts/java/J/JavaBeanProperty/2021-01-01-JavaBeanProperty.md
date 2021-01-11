---
title: JavaBeanProperty
permalink: Java/JavaBeanProperty
date: 2021-01-11
key: JavaJava.J.JavaBeanProperty
category: java
tags: ['java se', 'javafx.beans.property.adapter', 'javafx.base', 'interface java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JavaBeanProperty.description }}

## Sintaxis
~~~java
public interface JavaBeanProperty<T> extends ReadOnlyJavaBeanProperty<T>, Property<T>
~~~

## Ejemplo
~~~java
{{ site.data.Java.J.JavaBeanProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaBeanProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
