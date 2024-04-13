---
title: EventSetDescriptor.EventSetDescriptor()
permalink: /Java/EventSetDescriptor/EventSetDescriptor/
date: 2021-01-11
key: Java.E.EventSetDescriptor
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EventSetDescriptor.constructores valor="EventSetDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public EventSetDescriptor(Class<?> sourceClass, String eventSetName, Class<?> listenerType, String listenerMethodName) throws IntrospectionException
public EventSetDescriptor(Class<?> sourceClass, String eventSetName, Class<?> listenerType, String[] listenerMethodNames, String addListenerMethodName, String removeListenerMethodName) throws IntrospectionException
public EventSetDescriptor(Class<?> sourceClass, String eventSetName, Class<?> listenerType, String[] listenerMethodNames, String addListenerMethodName, String removeListenerMethodName, String getListenerMethodName) throws IntrospectionException
public EventSetDescriptor(String eventSetName, Class<?> listenerType, MethodDescriptor[] listenerMethodDescriptors, Method addListenerMethod, Method removeListenerMethod) throws IntrospectionException
public EventSetDescriptor(String eventSetName, Class<?> listenerType, Method[] listenerMethods, Method addListenerMethod, Method removeListenerMethod) throws IntrospectionException
public EventSetDescriptor(String eventSetName, Class<?> listenerType, Method[] listenerMethods, Method addListenerMethod, Method removeListenerMethod, Method getListenerMethod) throws IntrospectionException
~~~

## Parámetros
* **String getListenerMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String getListenerMethodName" %}
* **Method[] listenerMethods**,  {% include w3api/param_description.html metodo=_dato parametro="Method[] listenerMethods" %}
* **Method getListenerMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method getListenerMethod" %}
* **String removeListenerMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String removeListenerMethodName" %}
* **Class&lt;?&gt; sourceClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> sourceClass" %}
* **String addListenerMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String addListenerMethodName" %}
* **String[] listenerMethodNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] listenerMethodNames" %}
* **String listenerMethodName**,  {% include w3api/param_description.html metodo=_dato parametro="String listenerMethodName" %}
* **Method addListenerMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method addListenerMethod" %}
* **MethodDescriptor[] listenerMethodDescriptors**,  {% include w3api/param_description.html metodo=_dato parametro="MethodDescriptor[] listenerMethodDescriptors" %}
* **Method removeListenerMethod**,  {% include w3api/param_description.html metodo=_dato parametro="Method removeListenerMethod" %}
* **Class&lt;?&gt; listenerType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> listenerType" %}
* **String eventSetName**,  {% include w3api/param_description.html metodo=_dato parametro="String eventSetName" %}

## Excepciones
[IntrospectionException](/Java/IntrospectionException/)

## Clase Padre
[EventSetDescriptor](/Java/EventSetDescriptor/)

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
