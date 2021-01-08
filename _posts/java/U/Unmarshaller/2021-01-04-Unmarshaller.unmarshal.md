---
title: Unmarshaller.unmarshal()
permalink: Java/Unmarshaller/unmarshal
date: 2021-01-04
key: JavaJava.U.Unmarshaller
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.Unmarshaller.metodos valor="unmarshal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object unmarshal(File f) throws JAXBException
Object unmarshal(InputStream is) throws JAXBException
Object unmarshal(Reader reader) throws JAXBException
Object unmarshal(URL url) throws JAXBException
Object unmarshal(XMLEventReader reader) throws JAXBException
<T> JAXBElement<T> unmarshal(XMLEventReader reader, Class<T> declaredType)
Object unmarshal(XMLStreamReader reader) throws JAXBException
<T> JAXBElement<T> unmarshal(XMLStreamReader reader, Class<T> declaredType)
Object unmarshal(Source source) throws JAXBException
<T> JAXBElement<T> unmarshal(Source source, Class<T> declaredType)
Object unmarshal(Node node) throws JAXBException
<T> JAXBElement<T> unmarshal(Node node, Class<T> declaredType)
Object unmarshal(InputSource source) throws JAXBException
~~~

## Parámetros
* **Class&lt;T&gt; declaredType**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> declaredType" %}
* **XMLStreamReader reader**,  {% include w3api/param_description.html metodo=_data parametro="XMLStreamReader reader" %}
* **Source source**,  {% include w3api/param_description.html metodo=_data parametro="Source source" %}
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **File f**,  {% include w3api/param_description.html metodo=_data parametro="File f" %}
* **InputStream is**,  {% include w3api/param_description.html metodo=_data parametro="InputStream is" %}
* **Node node**,  {% include w3api/param_description.html metodo=_data parametro="Node node" %}
* **InputSource source**,  {% include w3api/param_description.html metodo=_data parametro="InputSource source" %}
* **XMLEventReader reader**,  {% include w3api/param_description.html metodo=_data parametro="XMLEventReader reader" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_data parametro="Reader reader" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnmarshalException](/Java/UnmarshalException/), [IllegalStateException](/Java/IllegalStateException/), [JAXBException](/Java/JAXBException/)

## Clase Padre
[Unmarshaller](/Java/Unmarshaller/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.Unmarshaller.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
